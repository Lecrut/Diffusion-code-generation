def repeat_instructions():
    for i in range(5):
        if i % 2 == 0:
            print(f"Even number: {i}")
        else:
            print(f"Odd number: {i}")

if __name__ == '__main__':
    repeat_instructions()