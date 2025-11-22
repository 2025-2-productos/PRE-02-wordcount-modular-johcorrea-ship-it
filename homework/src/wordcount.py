# obtain a list of files in the input directory

from homework.src._internals.count_words import count_words
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words

from ._internals.write_count_words import write_count_words


def main():
    ## mover a la funcion read all lines
    all_lines = read_all_lines()

    ### mover a la funcion preprocess lines
    all_lines = preprocess_lines(all_lines)

    ### mover a la funcionsplit in words
    words = split_into_words(all_lines)

    ### mover a la funcion count words
    counter = count_words(words)

    ### mover a la funcion write count words

    write_count_words(counter)


if __name__ == "__main__":
    main()
