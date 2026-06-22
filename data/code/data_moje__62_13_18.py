def get_divisors(n):
    if n == 0:
        return []
    result = []
    if n < 0:
        n = -n
    step = 1 if n % 2 != 0 else 2
    limit = int(n**0.5)
    for i in range(1, limit + 1, step if n % 2 != 0 else 1):
        if i == 1:
            result.append(1)
            if n > 1:
                result.append(n)
        else:
            if n % i == 0:
                result.append(i)
                j = n // i
                if j != i:
                    result.append(j)
    if step != 1:
        for i in range(2, limit + 1, 2):
            if n % i == 0:
                result.append(i)
                j = n // i
                if j != i:
                    result.append(j)
    result.sort()
    return list(set(result))

def get_divisors_optimized(n):
    if n == 0:
        return []
    result = []
    abs_n = abs(n)
    limit = int(abs_n**0.5)
    for i in range(1, limit + 1):
        if abs_n % i == 0:
            result.append(i)
            j = abs_n // i
            if i != j:
                result.append(j)
    result.sort()
    return result

if __name__ == '__main__':
    sample_number = 28
    divs = get_divisors_optimized(sample_number)
    print(divs)