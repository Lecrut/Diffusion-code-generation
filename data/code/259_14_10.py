def get_extremes(lst):
    return (min(lst), max(lst)) if lst else None

if __name__ == '__main__':
    sample_list = [12, 45, 7, 98, 3]
    extremes = get_extremes(sample_list)
    print(f"Smallest: {extremes[0]}")
    print(f"Largest: {extremes[1]}")