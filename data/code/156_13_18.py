average = lambda nums: sum(nums) / len(nums) if nums else 0

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 5.0]
    try:
        print(average(sample_values))
    except ZeroDivisionError:
        print("Cannot compute average for an empty list.")