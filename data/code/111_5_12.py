from datetime import date

class Person:
    def __init__(self, birth_date):
        self.birth_date = birth_date

    def calculate_age(self):
        today = date(2024, 1, 1)
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

if __name__ == '__main__':
    person = Person(date(1990, 3, 15))
    print(person.calculate_age())