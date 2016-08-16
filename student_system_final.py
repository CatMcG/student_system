import datetime
import json
import webbrowser

# TODO: General - check for input TypeErrors

class Student(object):

    def make_forename(self):

        self.forename = input('Forename: ')

    def make_surname(self):

        self.surname = input('Surname: ')

    def make_gender(self):

        self.gender = input('Gender (M/F): ')

# TODO: create an array of choices M, F... etc and check input?

    def make_dob(self):

        dob_string = input('Date of Birth (dd/mm/yyyy) ')
        birth_day = int(dob_string[0:2])
        birth_month = int(dob_string[3:5])
        birth_year = int(dob_string[6:10])
        self.dob = '{}-{}-{}'.format(birth_day, birth_month, birth_year)
        dob_datetime = datetime.date(birth_year, birth_month, birth_day)
        return dob_datetime

# TODO: datetime object specified in task but unable to convert this to json. Have created string version for outputting
# TODO: to json and a datetime object for calculating age. May need to find another way around this.

    def make_age(self):

        dob = self.make_dob()
        today = datetime.date.today()
        if today.year >= dob.year:
            if today.month > dob.month:
                self.age = today.year - dob.year
            elif today.month == dob.day:
                if today.day >= dob.day:
                    self.age = today.year - dob.year
            else:
                self.age = (today.year - dob.year) - 1
        else:
            self.age = 0

    def make_year(self):

        self.year = input('Year (7, 8, 9, 10 or 11): ')

# TODO: create an array of year choices and check input?

    def make_year_class(self):

        self.year_class = input('Class (A, B, C, D or E): ')

# TODO: create an array of class choices and check input?

    def make_search_key(self):

        search_forename = input('Forename: ')
        search_surname = input('Surname: ')
        search_key = make_key(search_forename,search_surname)
        return search_key

    def read_student(self):

        search_key = self.make_search_key()
        filename = '{}.json'.format(search_key)
        with open(filename, 'rU') as f:
            student_json = f.read()
        student_dict = json.loads(student_json)
        return student_dict

    def load_student(self):

# TODO: Could put all this in a for loop

        student_dict = self.read_student()
        if 'forename' in student_dict.keys():
            self.forename = student_dict['forename']
            print('Forename = {}'.format(self.forename))

        if 'surname' in student_dict.keys():
            self.surname = student_dict['surname']
            print('Surname = {}'.format(self.surname))

        if 'dob' in student_dict.keys():
            self.dob = student_dict['dob']
            print('Date of Birth = {}'.format(self.dob))

        if 'gender' in student_dict.keys():
            self.gender = student_dict['gender']
            print('Gender = {}'.format(self.gender))

        if 'year_class' in student_dict.keys():
            self.year_class = student_dict['year_class']
            print('Class = {}'.format(self.year_class))

        if 'year' in student_dict.keys():
            self.year = student_dict['year']
            print('Year = {}'.format(self.year))

        if 'age' in student_dict.keys():
            self.age = student_dict['age']
            print('Age = {}'.format(self.age))

        if 'predicted_results' in student_dict.keys():
            self.predicted_results = student_dict['predicted_results']
            print('Predicted Results ={}'.format(self.predicted_results))

        if 'final_results' in student_dict.keys():
            self.final_results = student_dict['final_results']
            print('Final Results ={}'.format(self.final_results))



    def input_predicted_results(self):

        subjects = subject_list()
        predicted_results_dict = {}
        option = input('Add predicted results? (y/n): ')
        if option == 'y':
            for subject in subjects:
                predicted_results_dict[subject] = float(input('{} (%): '.format(subject)))
            self.predicted_results = predicted_results_dict
            print('Student amended.')
        if option == 'n':
            print('No predicted results added')

    def input_final_results(self):

        subjects = subject_list()
        final_results_dict = {}
        option = input('Add final results? (y/n): ')
        if option == 'y':
            for subject in subjects:
                final_results_dict[subject] = float(input('{}{}'.format(subject, ': ')))
            self.final_results = final_results_dict
            print('Student amended.')
        if option == 'n':
            print('No final results added')

    def make_results_card(self):

        subjects = subject_list()
        results_table = ''

        for subject in subjects:
            row = '<tr><td>{}</td><td>{}</td></tr>'.format(subject, self.final_results[subject])
            results_table = '{}{}'.format(results_table, row)

        university = "University of Manchester"
        title = 'Exam Results 2016'
        student_name = '{} {} ({})'.format(self.forename, self.surname, self.gender)
        dob = '{} (Age: {})'.format(self.dob, self.age)
        year_group = '{}{}'.format(self.year, self.year_class)
        table_style = "<style> table {font-family: arial, sans-serif; border-collapse: collapse; width: 100%;} td, th " \
                      "{ border: 1px solid #dddddd; text-align: left; padding: 8px;} tr:nth-child(even) " \
                      "{ background-color: #dddddd; } </style>"
        results_card='{}{}_results.html'.format(self.forename,self.surname)

        f = open(results_card, 'w')

        message = """<!DOCTYPE html>
        <html>
        <head>
        {table_style}
        </head>
        <body>
        <h1>{university}</h1>
        <h2>{title}</h2>
        <p><b>Name</b>: {student_name}</p></body>
        <p><b>Date of Birth</b>: {dob}</p></body>
        <p><b>Class</b>: {year_group}</p></body>
        <table>
        <tr>
        <th>Subject</th>
        <th>Result</th>
        </tr>
        {results_table}
        </table>
        </html>""".format(table_style=table_style, university=university, title=title, student_name=student_name,
                          dob=dob, year_group=year_group, results_table=results_table)

        f.write(message)
        f.close()

    def open_results_card(self):

#TODO Make this work!

        new = 2  # open in a new tab, if possible
        results_card = '{}{}_results.html'.format(self.forename,self.surname)
        webbrowser.open(results_card, new=new)

    def performance_review(self):

        subjects = subject_list()
        subject_review_dict = {}
        performance_score = 0
        for subject in subjects:
            grade_diff = float(self.final_results[subject]) - float(self.predicted_results[subject])
            subject_review_dict[subject] = grade_diff
            performance_score += grade_diff
            print('{}: {} %'.format(subject, "%+d" % grade_diff))
        self.subject_review = subject_review_dict
        self.performance_score = performance_score
        print('Performance Score = {}'.format("%+d" % performance_score))

    def performance_ranking(self):

        student_index = make_index()
        print(student_index.keys())
        ranking_dict={}
        for student in student_index.keys():
            with open (student_index[student], 'rU') as f:
                student_json = f.read()
                student_dict = json.loads(student_json)
                name = '{} {}'.format(student_dict['forename'], student_dict['surname'])
                #print(student_dict)
                if 'performance_score' in student_dict.keys():
                    ranking_dict[name] = student_dict['performance_score']
                else:
                    ranking_dict[student] = 0
        ranking_dict_sorted = sorted(ranking_dict, key=ranking_dict.get, reverse=True)
        for student in ranking_dict_sorted:
            print('{}: {}'.format(student, ranking_dict[student]))

# TODO Try and incorporate the load_student function as some code is repeated

    def save(self):

        student_key = make_key(self.forename, self.surname)
        student_json = json.dumps(self, default=j_default)
        student_file = '{}.json'.format(student_key)
        with open(student_file, 'w') as f:
            f.write(student_json)
        #print(student_json)
        with open('student_index.json', 'a') as f:
            f.write(json.dumps('{}:{}'.format(student_key,student_file)))
        print('Student saved.')
        #print(json.dumps('{}:{}'.format(student_key,student_file)))



    def make_student(self):

        self.make_forename()
        self.make_surname()
        self.make_gender()
        self.make_age()
        self.make_year()
        self.make_year_class()
        self.save()
        cont()

    def run_predicted_results(self):

        self.load_student()
        self.input_predicted_results()
        self.save()
        cont()

    def run_final_results(self):

        self.load_student()
        self.input_final_results()
        self.save()
        cont()

    def run_performance_review(self):

        self.load_student()
        self.performance_review()
        self.save()
        cont()

    def run_performance_ranking(self):
    #
        self.performance_ranking()
        cont()


    def run_report_card(self):

        self.load_student()
        self.make_results_card()
        cont()

    def run_open_report_card(self):

        self.load_student()
        self.open_results_card()
        cont()

def make_index():
    filename = 'student_index.json'
    with open(filename, 'rU') as f:
        student_index_file = f.read()
    student_index_split = student_index_file.split('"')[1::2]
    student_index = {}
    for item in student_index_split:
        item_split = item.split(':')
        index_key = item_split[0]
        index_value = item_split[1]
        student_index[index_key] = index_value
    # print('{}:{}'.format(index_key, index_value))
    return student_index

def subject_list():

    subjects = [
        'English',
        'Mathematics',
        'Science',
        'Art and Design',
        'Citizenship',
        'Computing',
        'Design and Technology',
        'Geography',
        'History',
        'French',
        'Spanish',
        'German',
        'Music',
        'Physical Education', ]
    return subjects

# Converts class object to a dictionary:

def j_default(o):

    return o.__dict__

def make_key(forename, surname):

    student_key = '{}{}'.format(forename, surname)
    return (student_key)

def cont():

    cont_opt = (input('Select another action? (y/n): '))

    if cont_opt == 'y':
        main()
    elif cont_opt == 'n':
        print('Thank you for using the student system')
    else:
        print('Invalid')


def main():

    student_instance=Student()

# TODO Put available functions in an interactive menu

    print('Welcome to the student system. The following actions are available:\n\n'
          '1 - Add new student.\n'
          '2 - Add predicted results.\n'
          '3 - Add final results.\n'
          '4 - Run performance review.\n'
          '5 - View perfomance rankings.\n'
          '6 - Create report card. \n')

    option = input('Please select an action (1-6): ')

    if option=='1':
        student_instance.make_student()
    elif option=='2':
        student_instance.run_predicted_results()
    elif option=='3':
        student_instance.run_final_results()
    elif option=='4':
        student_instance.run_performance_review()
    elif option=='5':
        student_instance.run_performance_ranking()
    elif option=='6':
        student_instance.run_report_card()
    else:
        print('Not Valid')




    # student_instance.make_student()
    # student_instance.run_predicted_results()
    # student_instance.run_final_results()
    # student_instance.run_performance_review()
    # student_instance.run_performance_ranking()

# TODO Still need to make the ranked performance list

    # student_instance.run_report_card()
    # student_instance.run_open_report_card() # doesn't work

if __name__ == "__main__": main()