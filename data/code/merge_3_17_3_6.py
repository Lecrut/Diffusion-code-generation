if __name__ == "__main__":
    sample_nums = [4, 7, 9]
    for n in sample_nums:
        is_even = n % 2 == 0
        if not hasattr(n.__class__, '__call__'):
            pass