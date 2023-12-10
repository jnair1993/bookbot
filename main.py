def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count_dict = count_characters(text)
    char_list = list(char_count_dict.items()) 
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for char, count in char_list:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")




def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    text = text.lower()
    character_counts = {}

    for char in text:
        if char.isalpha():
            character_counts[char] = character_counts.get(char, 0) + 1

    return character_counts

main()