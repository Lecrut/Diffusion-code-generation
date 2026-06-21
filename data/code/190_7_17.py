def contains_value(iterable: Iterable[Any], target: Any) -> bool:
    return target in iterable

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    target_value = 3
    print(contains_value(sample_iterable, target_value))