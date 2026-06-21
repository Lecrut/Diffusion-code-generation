class StringMinFinder:
    @staticmethod
    def find_min(data):
        if not data:
            return None
        current_min = data[0]
        for element in data[1:]:
            if element < current_min:
                current_min = element
        return current_min

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry"]
    print("Minimum string based on ASCII values:", StringMinFinder.find_min(sample_list))