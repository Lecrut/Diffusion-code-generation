BASE_SCALE = 1
HEIGHT_SCALE = 1

parallelogram_area = lambda base, height: (base * BASE_SCALE) * (height * HEIGHT_SCALE)

if __name__ == '__main__':
    result = parallelogram_area(10, 5)
    print(result)