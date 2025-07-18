from WordLang import WordLang
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m WordLang 'your sentence here'")
        return
    text = " ".join(sys.argv[1:])
    wl = WordLang(text)
    
    print("Text:", wl.text)
    print("Sentiment:", wl.sentiment.analyze())
    print("Polarity:", wl.sentiment.polarity)
    print("Sentence form:", wl.sentiment.sentence())
    print("Word types:", wl.grammar.wordtypes())
    print("Shuffled:", wl.transform.shuffle())
    print("Reversed:", wl.reverse())

if __name__ == "__main__":
    main()