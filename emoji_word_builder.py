from collections import OrderedDict


# This script uses the public-domain ENABLE word list
# http://www.puzzlers.org/dokuwiki/doku.php?id=solving:wordlists:about:enable_readme
with open('enable_wordlist.txt', 'rb') as file_:
    all_words = file_.read().lower().split()

# These are all emoji that have letters in them in major typefaces, according to
# http://unicode.org/emoji/charts/full-emoji-list.html
EMOJI_SUBSTRINGS = {
    'abcd': u'\U0001F520', # INPUT SYMBOL FOR LATIN CAPITAL LETTERS
    # 'abcd': u'\U0001F521', # INPUT SYMBOL FOR LATIN SMALL LETTERS; duplicate
    'back': u'\U0001F519', # BACK WITH LEFTWARDS ARROW ABOVE
    'cool': u'\U0001F192', # SQUARED COOL
    'free': u'\U0001F193', # SQUARED FREE
    'soon': u'\U0001F51C', # SOON WITH RIGHTWARDS ARROW ABOVE
    # 'abc': u'\U0001F524', # INPUT SYMBOL FOR LATIN LETTERS; 'a' plus 'b' plus 'c'
    'atm': u'\U0001F3E7', # AUTOMATED TELLER MACHINE
    'end': u'\U0001F51A', # END WITH LEFTWARDS ARROW ABOVE
    'new': u'\U0001F195', # SQUARED NEW
    'off': u'\U0001F4F4', # MOBILE PHONE OFF
    'sos': u'\U0001F198', # SQUARED SOS
    'top': u'\U0001F51D', # TOP WITH UPWARDS ARROW ABOVE
    'zzz': u'\U0001F4A4', # SLEEPING SYMBOL
    # 'ab': u'\U0001F18E', # NEGATIVE SQUARED AB; 'a' plus 'b'
    'cl': u'\U0001F191', # SQUARED CL
    'id': u'\U0001F194', # SQUARED ID
    'ng': u'\U0001F196', # SQUARED NG
    'ok': u'\U0001F197', # SQUARED OK
    'on': u'\U0001F51B', # ON WITH EXCLAMATION MARK WITH LEFT RIGHT ARROW ABOVE
    'tm': u'\U00002122', # TRADE MARK SIGN
    'up': u'\U0001F199', # SQUARED UP WITH EXCLAMATION MARK
    'vs': u'\U0001F19A', # SQUARED VS
    'wc': u'\U0001F6BE', # WATER CLOSET
    'a': u'\U0001F170', # NEGATIVE SQUARED LATIN CAPITAL LETTER A
    'b': u'\U0001F171', # NEGATIVE SQUARED LATIN CAPITAL LETTER B
    'c': u'\U000000A9', # COPYRIGHT SIGN
    'i': u'\U00002139', # INFORMATION SOURCE
    'm': u'\U000024C2', # CIRCLED LATIN CAPITAL LETTER M
    # 'm': u'\U0000303D', # PART ALTERNATION MARK
    'o': u'\U0001F17E', # NEGATIVE SQUARED LATIN CAPITAL LETTER O
    'p': u'\U0001F17F', # NEGATIVE SQUARED LATIN CAPITAL LETTER P
    'r': u'\U000000AE', # REGISTERED SIGN
    'x': u'\U0000274C', # CROSS MARK
}

def can_word_be_built (remaining_text, emoji_built_word=''):
    if remaining_text == '':
        return emoji_built_word
    else:
        for substring, emoji in EMOJI_SUBSTRINGS.iteritems():
            if remaining_text.startswith(substring):
                remaining_text = remaining_text[len(substring):]
                return can_word_be_built(remaining_text, emoji_built_word + emoji)
                break
        else:
            return False

can_be_built = OrderedDict()
for word in all_words:
    built_word = can_word_be_built(word)
    if built_word:
        can_be_built[word] = built_word

max_length = max(len(word) for word in can_be_built.keys())
for length in range(2, max_length + 1):
    print('Words of length {}:'.format(length))
    for word, emoji in can_be_built.iteritems():
        if len(word) == length:
            print(u'{} - {}'.format(word, emoji))
