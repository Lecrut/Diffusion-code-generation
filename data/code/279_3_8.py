class PersonAgePrinter:
    def __init__(self, people):
        self.people = people

    def print_ages(self):
        for name, age in self.people.items():
            print(f"{name}: {age}")

if __name__ == '__main__':
    sample_people = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }
    printer = PersonAgePrinter(sample_people)
    printer.print_ages()