import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o")
text = "Artificial intelligence is transforming software engineering."
text2 = "कृत्रिम बुद्धिमत्ता सॉफ्टवेयर इंजीनियरिंग को बदल रही है।"
tokens1 = enc.encode(text)
tokens2 = enc.encode(text2)
print("Tokens len: ", len(tokens1))
print("Hindi Tokens: ", len(tokens2))
decode1 = enc.decode(tokens1)
decode2 = enc.decode(tokens2)