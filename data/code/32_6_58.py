class StringHelper:
    @staticmethod
    def validate_input(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")

    @staticmethod
    def calculate_length(s):
        StringHelper.validate_input(s)
        return len(s)

if __name__ == '__main__':
    sample_string1 = "Data Science"
    sample_string2 = "Machine Learning"

    try:
        length1 = StringHelper.calculate_length(sample_string1)
        print(f"Length of '{sample_string1}': {length1}")

        length2 = StringHelper.calculate_length(sample_string2)
        print(f"Length of '{sample_string2}': {length2}")
    except ValueError as e:
        print(e)