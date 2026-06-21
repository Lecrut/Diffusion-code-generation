class StringMerger:
    def __init__(self, first_part, second_part):
        if not all(isinstance(part, str) for part in (first_part, second_part)):
            raise ValueError("Both inputs must be strings.")
        self.first_part = first_part
        self.second_part = second_part

    def merge(self):
        return self.first_part + self.second_part

    def get_parts(self):
        return self.first_part, self.second_part

if __name__ == '__main__':
    merger = StringMerger("Good evening, ", "World!")
    print(merger.merge())
    first, second = merger.get_parts()
    print(f"First part: {first}")
    print(f"Second part: {second}")