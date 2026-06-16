def satisfies_condition(iterable, condition):
    return any(condition(item) for item in iterable)
if __name__ == '__main__':
    sample_list = [10, 25, -3.7, True]
    def is_positive(x):
        return x > 0
    result = satisfies_condition(sample_list, is_positive)
    print(result)