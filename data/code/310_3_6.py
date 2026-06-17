def file_content_generator(file1, file2):
    for chunk in file1:
        yield chunk
    for chunk in file2:
        yield chunk
if __name__ == '__main__':
    import io
    data1 = b"This is the content of the first file.\n" + b"A much longer string to simulate a large file." * 100000
    data2 = b"This is the content of the second file.\n" + b"Another very long piece of data for the second file." * 100000
    file1_obj = io.BytesIO(data1)
    file2_obj = io.BytesIO(data2)
    generator = file_content_generator(file1_obj, file2_obj)
    collected_chunks = []
    for chunk in generator:
        collected_chunks.append(chunk)
    print("--- Contents yielded by the generator ---")
    for i, chunk in enumerate(collected_chunks):
        print(f"Chunk {i}: {chunk}")