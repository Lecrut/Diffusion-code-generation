EVEN_THRESHOLD = 0

def check_evenness(n):
    return n % 2 == EVEN_THRESHOLD

if __name__ == '__main__':
    sample_values = [10, 15, 22, 33]
    results = {n: check_evenness(n) for n in sample_values}
    print(results)