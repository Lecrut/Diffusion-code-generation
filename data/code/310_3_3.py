def file_content_generator(file1, file2):
    for chunk in file1:
        yield chunk
    for chunk in file2:
        yield chunk
if __name__ == '__main__':
    import io
    data1 = b"This is the content of the first file.\n" + b"A very long string to test memory efficiency.\n" * 1000000
    data2 = b"This is the content of the second file.\n" + b"Another large block of data." * 500000
    file1 = io.BytesIO(data1)
    file2 = io.BytesIO(data2)
    generator = file_content_generator(file1, file2)
    collected_data = bytearray()
    for chunk in generator:
        collected_data.extend(chunk)
    print("--- Collected Data ---")
    print(collected_data.decode('utf-8'))