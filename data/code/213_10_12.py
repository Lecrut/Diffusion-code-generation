from statistics import mean, median, stdev

def analyze_list(numbers):
    if not numbers:
        return None, None, None
    avg = mean(numbers)
    med = median(numbers)
    std_dev = stdev(numbers) if len(numbers) > 1 else 0
    return sum(numbers), avg, med, std_dev

if __name__ == '__main__':
    sample_list = [10, 25, 32, 8, 45]
    total, avg, med, stdev = analyze_list(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Average: {avg}")
    print(f"Median: {med}")
    print(f"Standard Deviation: {stdev}")