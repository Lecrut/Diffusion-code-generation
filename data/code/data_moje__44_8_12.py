def compute_mean(data: list[int]) -> float:
    return sum(data) / len(data)

if __name__ == '__main__':
    values = [10, 20, 30, 40, 50]
    result = compute_mean(values)
    print(result)