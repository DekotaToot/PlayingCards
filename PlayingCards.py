import random
royalty = ['king','queen','jack']
suits = ['heart','diamond','club','spade']
deck = []
for i in suits:
    deck += [[j,i] for j in range(1,11)] + [[j,i] for j in royalty]
def perfectCut(cards):
    split = len(cards) // 2
    return [cards[0:split],cards[split:]]
def perfectShuffle(cards,times):
    while times > 0:
        times -= 1
        cut = perfectCut(cards)
        if len(cut[0]) == len(cut[1]):
            cards=[]
            for i in range(len(cut[0])):
                cards.append(cut[0][i])
                cards.append(cut[1][i])
        else:
            cards=[]
            for i in range(len(cut[0])):
                cards.append(cut[0][i])
                if i == len(cut[0]) // 2:
                    cards.append(cut[1][len(cut[1]) - 1])
                cards.append(cut[1][i])
    return cards
def shuffle(cards,times):
    while times > 0:
        times -= 1
        cards = perfectShuffle(cards,1)
        steps = random.randint(2,8)
        while steps > 0:
            steps -= 1
            choiceOfCard = random.randint(0,len(cards) - 1)
            held = cards.pop(choiceOfCard)
            cards.insert(choiceOfCard + 1,held)
    return cards
