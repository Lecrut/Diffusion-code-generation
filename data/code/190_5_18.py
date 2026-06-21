def is_object_in_list(obj, obj_list):
    return any((id(obj) == id(item) for item in obj_list))
if __name__ == '__main__':

    class SampleClass:

        def __init__(self, value):
            self.value = value
    sample_obj = SampleClass(42)
    sample_list = [SampleClass(1), sample_obj, SampleClass(3)]
    print(is_object_in_list(sample_obj, sample_list))