def repeating_generator():
    predefined_list = [1, 2, 3, 4, 5]
    count = 0
    while True:
        for item in predefined_list:
            if count >= 50:
                return
            yield item
            count += 1

if __name__ == '__main__':
    gen = repeating_generator()
    result = [next(gen) for _ in range(50)]
    print(result)