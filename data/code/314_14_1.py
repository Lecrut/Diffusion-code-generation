def running_total(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result_generator = running_total(data)
    final_sum = sum(result_generator)
    print(f"Final sum calculated by generator: {final_sum}")