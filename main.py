import sys
from stats import get_num_words, get_char_counts, sort_char_counts
def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")
    char_counts = get_char_counts(book_text)
    for char in sorted(char_counts.keys()):
        print(f"'{char}': {char_counts[char]}")
    sorted_chars = sort_char_counts(char_counts)
    print("\nCharacter Frequency Report:")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")
if __name__ == "__main__":
    main()

