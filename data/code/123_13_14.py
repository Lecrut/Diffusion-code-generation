if __name__ == '__main__':
    start = 1
    end = 100
    if start < 1 or end <= start:
        raise ValueError("Invalid range. Start must be at least 1 and end must be greater than start.")
    
    sum_of_range = sum(x for x in range(start, end + 1))
    print(sum_of_range)