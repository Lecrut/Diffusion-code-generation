def contains_zero(iterable):
            for item in iterable:
                if item == 0:
                    yield True
                    return # Stops the generator immediately after yielding True
        
            # If we reach here, no zero was found during iteration
            yield False

if __name__ == '__main__':
    pass
