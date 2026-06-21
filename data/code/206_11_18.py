class MinFinder:
    @staticmethod
    def find_minimum(data):
        if not data:
            raise ValueError("Input list is empty")
        minimum = data[0]
        for item in data[1:]:
            if not isinstance(item, int):
                raise TypeError("All elements must be integers")
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    try:
        result = MinFinder.find_minimum(sample_list)
        print(result)
    except (ValueError, TypeError) as e:
        print(e)

    empty_list = []
    try:
        result_empty = MinFinder.find_minimum(empty_list)
        print(result_empty)
    except (ValueError, TypeError) as e:
        print(e)