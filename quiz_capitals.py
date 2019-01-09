import random

stolice = {'mazowieckiego' : 'Warszawa', 'pomorskiego' : 'Gdańsk', 'zachodnio-pomorskiego' : 'Szczecin', 'warmińsko-mazurskiego' : 'Olsztyn',
            'kujawsko-pomorskiego' : 'Bydgoszcz', 'wielkopolskiego' : 'Poznań', 'podlaskiego' : 'Białystok', 'dolnośląskiego' : 'Wrocław',
            'małopolskiego' : 'Kraków', 'opolskiego' : 'Opole', 'śląskiego' :  'Katowice', 'podkarpackiego' : 'Rzeszów', 'lubuskiego' : 'Gorzów Wielkopolski',
            'lubelskiego' : 'Lublin', 'świętokrzyskiego' : 'Kielce', 'łódzkiego' : 'Łódź'}


for quizNum in range(5):

    quizFile = open('stolicequiz{}.txt'.format(quizNum + 1), 'w', encoding='windows-1250')
    answerKeyFile = open('stolicequiz_answers{}.txt'.format(quizNum + 1), 'w')

    quizFile.write('Imię i nazwisko:\n\nData:\n\nKlasa:\n\n')
    quizFile.write((' ' * 20) + 'Quiz stolic województw Polski (From {})'.format(quizNum + 1))
    quizFile.write('\n\n')

    wojewodztwa = list(stolice.keys())
    random.shuffle(wojewodztwa)

    for questionNum in range(0, 16):

        correctAnswer = stolice[wojewodztwa[questionNum]]
        wrongAnswers = list(stolice.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write('{}. Co jest stolicą województwa {}?\n'.format(questionNum + 1, wojewodztwa[questionNum]))
        for i in range(0, 4):
            quizFile.write('  {}. {}\n'.format('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('{}. {}\n'.format(questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()





