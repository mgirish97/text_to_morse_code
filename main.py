import pandas as pd

chart = pd.read_csv('chart.csv', index_col='letter')


def translator():
    start = True
    print('Hello! Welcome to the Text to Morse Code Converter.')
    while start:
        text_or_morse = input('\nType in "Text" or "Morse" to convert either respectively '
                              'or type "end" to end the program:\n').lower()
        if text_or_morse == 'text':
            text = input('\nInput text you would like converted into Morse Code:\n')
            translate_to_morse(text)
        elif text_or_morse == 'morse':
            text = input('\nInput Morse Code you would like converted into text:\n')
            translate_to_text(text)
        elif text_or_morse == 'end':
            start = False
        else:
            print('\nPlease input a valid phrase.')


def translate_to_morse(text):
    translated = ''
    for i in text:
        if i.upper() in chart.index:
            translated += chart.loc[i.upper()].code + ' '
        else:
            continue
    translated = translated[:-1]
    print("Here's your translated text: \n")
    print(translated)


def translate_to_text(text):
    text_list = text.split()
    translated_text = ''
    for char in text_list:
        if char in chart.code.values:
            translated_text += chart[chart.code == char].index[0]
    print("Here's your translated morse: \n")
    print(translated_text)


translator()
    
    
