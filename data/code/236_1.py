def repeat_shape(shape_definition, repetition_count):
    result = ""
    for shape in shape_definition:
        result += shape
    return result * repetition_count
if __name__ == '__main__':
    shape1 = ["A", "B"]
    count1 = 3
    output1 = repeat_shape(shape1, count1)
    print(f"Shape: {shape1}, Count: {count1}, Output: {output1}")
    shape2 = ["X", "Y", "Z"]
    count2 = 2
    output2 = repeat_shape(shape2, count2)
    print(f"Shape: {shape2}, Count: {count2}, Output: {output2}")
    shape3 = ["Hello", "World"]
    count3 = 4
    output3 = repeat_shape(shape3, count3)
    print(f"Shape: {shape3}, Count: {count3}, Output: {output3}")