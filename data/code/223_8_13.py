class MaxFinder:
    @staticmethod
    def find_maximum(data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty.")
        return sorted(data_list, reverse=True)[0]

if __name__ == '__main__':
    sample_list_1 = [10, 5, 20, 8, 15]
    sample_list_2 = [-5, -1, -10, -3]
    sample_list_3 = [42]
    sample_list_4 = []
    print(f"List 1: {sample_list_1}")
    try:
        max1 = MaxFinder.find_maximum(sample_list_1)
        print(f"Maximum of List 1: {max1}")
    except ValueError as e:
        print(e)