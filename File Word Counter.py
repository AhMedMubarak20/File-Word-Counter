def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return 0

file_name = input("Enter the name of the file: ")
word_count = count_words(file_name)
print(f"Number of words in {file_name}: {word_count}")
