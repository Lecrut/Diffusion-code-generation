class ListMinimizer:
    @staticmethod
    def find_min(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return sorted(data)[0]

if __name__ == '__main__':
    sample_list = [3.14, -1.5, 2.718, -10.0, 0.5, 42.0]
    try:
        result = ListMinimizer.find_min(sample_list)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")