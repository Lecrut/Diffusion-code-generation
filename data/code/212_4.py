def min_max_generator(iterable):
    if not iterable:
        return
    current_min = None
    current_max = None
    for item in iterable:
        if current_min is None:
            current_min = item
            current_max = item
        else:
            if item < current_min:
                current_min = item
            if item > current_max:
                current_max = item
        yield current_min, current_max
if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    generator = min_max_generator(sample_data)
    for minimum, maximum in generator:
        print(f"Min: {minimum}, Max: {maximum}")