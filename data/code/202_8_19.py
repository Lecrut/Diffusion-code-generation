class ListProcessor:
    MAX_ERROR = "Input list cannot be empty"
    
    @staticmethod
    def find_max(data):
        if not data:
            raise ValueError(ListProcessor.MAX_ERROR)
        max_val = data[0]
        for item in data[1:]:
            if item > max_val:
                max_val = item
        return max_val

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, '10', -1]
    try:
        print(ListProcessor.find_max(sample_values))
    except ValueError as e:
        print(e)