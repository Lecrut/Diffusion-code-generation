def repeat_action(max_count):
    count = 0
    while count < max_count:
        print(f"Action {count + 1}")
        if count == 2:
            break
        count += 1

if __name__ == '__main__':
    repeat_action(3)