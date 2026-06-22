class MaxFinder:
    NO_NUMBERS = "No numbers provided"
    
    @staticmethod
    def find_max(numbers):
        if not numbers:
            return None
        
        max_value = numbers[0]
        for number in numbers[1:]:
            if number > max_value:
                max_value = number
        return max_value

if __name__ == '__main__':
    sample_data = "10 5 22 8 30 1"
    numbers = list(map(int, sample_data.split()))
    result = MaxFinder.find_max(numbers)
    print(result if result is not None else MaxFinder.NO_NUMBERS)