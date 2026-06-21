def get_third(iterable):
    try:
        return iterable[2]
    except (IndexError, TypeError):
        return next((x for i, x in enumerate(iterable) if i == 2), None)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_third(sample_list)
    print(result)