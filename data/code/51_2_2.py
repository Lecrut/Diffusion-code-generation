def build_number_pyramid():
    return [str(i) * i for i in range(1, 7)]

if __name__ == '__main__':
    result = build_number_pyramid()
    print(result)