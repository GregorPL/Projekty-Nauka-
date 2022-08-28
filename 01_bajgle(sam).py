import random

NUM_DIGITS = 3 # Ilu cyfrowa będzie zgadywana liczba 
MAX_GUESSES = 10 # Ile prób będzie miał gracz

def main():
    print(f'''Bajgle, logiczna gra na dedukcję. Mam na myśli {NUM_DIGITS}-cyfrową liczbę, w której nie powtarza się żadna z cyfr.
    Spróbuj ją odgadnąć. Oto wskazówki:
    Gdy mówię:  Oznacza to:
        Piko    Jedna cyfra jest poprawna, ale jest na złej pozycji.
        Fermi   Jedna cyfra jest poprawna i znajduje się w odpowiednim miejscu.
        Bajgle  Żadna cyfra nie jest poprawna.
    
    Na przykład, jeśli tajna liczba to 248, a Ty podasz liczbę 843,
    wskazówka będzie brzmieć Fermi Piko.''')

    while True:
        secretNum = getSecretNum(NUM_DIGITS)
        print(f'Mam na myśli {NUM_DIGITS}-cyfrową liczbę.')
        print(f'Masz {MAX_GUESSES} prób aby ją odgadnąć.')

        num_guesses = 1
        
        while num_guesses <= MAX_GUESSES:
            guess = ''

            while len(guess) < NUM_DIGITS or not guess.isdecimal():
                print(f'Próba #{num_guesses}')
                guess = input('> ')
            
            num_guesses += 1
            
            clues = getClues(guess, secretNum)
            print(clues)

            if guess == secretNum:
                break
        
            if num_guesses > MAX_GUESSES:
                print('Wykorzystałeś wszystkie próby!')
                print(f'Sekretna liczba to {secretNum}')
        
        print('Czy chcesz zagrać jeszcze raz? (tak lub nie)')
        if not input('> ').lower().startswith('t'):
            break
    print('Dziękuję za grę!')



def getSecretNum(num_digits: int):
    nums = list('0123456789')
    random.shuffle(nums)

    return ''.join(nums[:num_digits])

def getClues(guess, secretNum):

    if guess == secretNum:
        return 'Udało się!'
    
    clues = []

    for i in range(len(secretNum)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Piko')

    if len(clues) == 0:
        return 'Bajgle' # Brak poprawnych cyfr
    else:
        # Ustaw wskazówki w kolejności alfabetycznej
        # aby uniknąć dodatkowej podpowiedzi.
        clues.sort()
        # Wszystkie wskazówki połącz w jeden napis.
        return ' '.join(clues)


if __name__ == '__main__':
    main()