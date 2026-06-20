if __name__ == '__main__':
    start = 1
    end = 100
    
    def validate_range(start, end):
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Start and end must be integers.")
        if start < 1 or end > 100:
            raise ValueError("Range must be between 1 and 100 inclusive.")
    
    validate_range(start, end)
    
    result = sum(x for x in range(start, end + 1))
    print(result)