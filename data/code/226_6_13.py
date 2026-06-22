def repeating_elements():
    predefined_list = [1, 2, 3]
    count = 0
    while True:
        for item in predefined_list:
            yield item
            count += 1
            if count >= 50:
                return

if __name__ == '__main__':
    gen = repeating_elements()
    result = [next(gen) for _ in range(50)]
    print(result)