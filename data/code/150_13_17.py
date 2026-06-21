class StringFilter:
    TARGET = "example"

    @staticmethod
    def remove_target(data):
        return [item for item in data if item != StringFilter.TARGET]

if __name__ == '__main__':
    sample_data = ["apple", "banana", "cherry", "example", "date"]
    filtered_data = StringFilter.remove_target(sample_data)
    print(filtered_data)