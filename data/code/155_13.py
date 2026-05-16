def stream_sum(iterable):
    current_sum = 0
    for item in iterable:
        current_sum += item
        yield current_sum
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result_stream = stream_sum(data)
    final_sum = 0
    print("Streamed sums:")
    for s in result_stream:
        print(s)
        final_sum = s
    print("\nFinal sum (last yielded value):")
    print(final_sum)