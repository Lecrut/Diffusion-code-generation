def is_positive(value: float) -> bool:
    return value > 0
if __name__ == '__main__':
    sample_values = [10.5, -3.2, 0, 4e-8]
    for num in sample_values:
        result = is_positive(num)
        print(f"{num} is {'positive' if result else 'not positive'}")