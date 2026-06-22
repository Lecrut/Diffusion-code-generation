def get_parallelogram_area_lambda():
    return lambda base, height: base * height

if __name__ == '__main__':
    area_func = get_parallelogram_area_lambda()
    result = area_func(base=10, height=5)
    print(result)