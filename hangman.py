import random
import hangman_words
import hangman_art

print(hangman_art.logo)
words = hangman_words.word_list
chosen_word = random.choice(words)
lives = 6
list_ = list('_' * len(chosen_word))
end_game = False

while not end_game:
    guess= input('Guess a word? ').lower()
    for index, element in enumerate(chosen_word):
        if element == guess:
            list_[index] = chosen_word[index]
    if guess not in chosen_word:
        lives -= 1
        if lives <= 0:
            end_game = True
            print(f"You Lost!,The correct word was '{chosen_word}'")
    if '_' not in list_:
        end_game = True
        print('You Win!')
        
    print(''.join(list_))
    print(hangman_art.stages[lives])