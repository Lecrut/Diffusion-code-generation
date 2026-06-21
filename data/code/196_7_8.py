def concatenate_generators(gen1, gen2):
    for item in gen1:
        yield item
    for item in gen2:
        yield item

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    generator1 = (item * 2 for item in list1)
    generator2 = (item + 10 for item in list2)
    
    concatenated_gen = concatenate_generators(generator1, generator2)
    
    result = []
    for item in concatenated_gen:
        result.append(item)
    
    print(f"Concatenated Result: {result}")