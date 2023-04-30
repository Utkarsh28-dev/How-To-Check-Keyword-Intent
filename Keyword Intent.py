import spacy

nlp = spacy.load("en_core_web_sm")

def check_intent(text):
    doc = nlp(text)
    for token in doc:
        if token.dep_ == "ROOT":
            if token.pos_ == "VERB":
                return "action"
            else:
                return "informational"
    return "unknown"

# Example usage
text1 = "What is the weather like today?"
text2 = "Book a table at a restaurant for 6pm tonight"
text3 = "How tall is the Eiffel Tower?"

print(check_intent(text1)) # informational
print(check_intent(text2)) # action
print(check_intent(text3)) # informational
