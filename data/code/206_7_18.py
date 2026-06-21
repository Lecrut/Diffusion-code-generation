class MinFinder:
    @staticmethod
    def find_min(data):
        if not data:
            raise ValueError("Data list cannot be empty")
        current_min = data[0]
        for element in data[1:]:
            if element < current_min:
                current_min = element
        return current_min

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print("Minimum value based on ASCII:", MinFinder.find_min(sample_list))