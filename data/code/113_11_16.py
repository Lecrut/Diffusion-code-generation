MINUEND = 10**100
SUBTRAHEND = 5 * 10**99

def subtract_large_integers(minuend: int, subtrahend: int) -> int:
    return minuend - subtrahend

if __name__ == '__main__':
    result = subtract_large_integers(MINUEND, SUBTRAHEND)
    print(result)