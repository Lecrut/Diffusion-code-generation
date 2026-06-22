def log_extremes(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Input parameters: args={args}, kwargs={kwargs}")
        print(f"Returned value: {result}")
        return result
    return wrapper

class MaxFinder:
    @staticmethod
    @log_extremes
    def find_max(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        maximum = data[0]
        for number in data:
            if number > maximum:
                maximum = number
        return maximum

if __name__ == '__main__':
    sample_list = [3.14159, 1.61803, 2.71828, -0.57721, 100.0, -5.2]
    try:
        max_val = MaxFinder.find_max(sample_list)
        print(f"The list is: {sample_list}")
        print(f"Maximum element: {max_val}")
    except ValueError as e:
        print(e)