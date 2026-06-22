def get_extremes(lst):
    return (min(lst), max(lst)) if lst else None

if __name__ == '__main__':
    sample_values = [10, 5, 22, 8, 15]
    extremes = get_extremes(sample_values)
    print(f"Smallest: {extremes[0]}")
    print(f"Largest: {extremes[1]}")