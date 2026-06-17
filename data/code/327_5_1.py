import time
def running_total(sequence):
    running_sum = 0
    running_totals = []
    for element in sequence:
        running_sum += element
        running_totals.append(running_sum)
    return running_totals
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = running_total(data)
    print(result)