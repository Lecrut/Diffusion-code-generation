class MaxFinder:
    def __init__(self, data_list):
        self.data_list = data_list

    def find_maximum(self):
        if not self.data_list:
            raise ValueError("Input list cannot be empty.")
        sorted_data = sorted(self.data_list, reverse=True)
        return sorted_data[0]

if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 8, 15]
    sample_list_2 = [-5, -1, -10, -3]
    sample_list_3 = [42]
    sample_list_4 = []

    finder = MaxFinder(sample_list_1)
    print(f"List 1: {sample_list_1}")
    try:
        max1 = finder.find_maximum()
        print(f"Maximum of List 1: {max1}\n")
    except ValueError as e:
        print(e)

    finder = MaxFinder(sample_list_2)
    print(f"List 2: {sample_list_2}")
    try:
        max2 = finder.find_maximum()
        print(f"Maximum of List 2: {max2}\n")
    except ValueError as e:
        print(e)

    finder = MaxFinder(sample_list_3)
    print(f"List 3: {sample_list_3}")
    try:
        max3 = finder.find_maximum()
        print(f"Maximum of List 3: {max3}\n")
    except ValueError as e:
        print(e)

    finder = MaxFinder(sample_list_4)
    print(f"List 4: {sample_list_4}")
    try:
        max4 = finder.find_maximum()
        print(f"Maximum of List 4: {max4}\n")
    except ValueError as e:
        print(e)