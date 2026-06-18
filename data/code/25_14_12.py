def gen(start, end):
            for n in range(start, end + 1):
                if n % 2 == 0: # It is an even number
                    if n == 0: 
                        yield True

if __name__ == '__main__':
    pass
