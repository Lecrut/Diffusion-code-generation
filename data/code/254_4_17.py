class StringMinimizer:
    @staticmethod
    def min_by_length(strings):
        if not strings:
            return None
        min_string = strings[0]
        for string in strings:
            if len(string) < len(min_string):
                min_string = string
        return min_string

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry", "date"]
    print(StringMinimizer.min_by_length(sample_values))