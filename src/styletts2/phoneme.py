from gruut import sentences
from collections.abc import Iterable
import phonemizer as ph
from phonemizer.separator import Separator


class PhonemeConverter:
    def phonemize(self, text):
        pass


class GruutPhonemizer(PhonemeConverter):
    def phonemize(self, text, lang='en-us'):
        phonemized = []
        for sent in sentences(text, lang=lang):
            for word in sent:
                if isinstance(word.phonemes, Iterable):
                    phonemized.append(''.join(word.phonemes))
                elif isinstance(word.phonemes, str):
                    phonemized.append(word.phonemes)
        phonemized_text = ' '.join(phonemized)
        return phonemized_text


class CustomPhonemizer(PhonemeConverter):
    def phonemize(self, text):
        return ph.phonemize(
            text,
            language="en-us",
            backend="espeak",
            preserve_punctuation=True,
            separator=Separator(phone='', word=' ', syllable=''),
        )


class PhonemeConverterFactory:
    @staticmethod
    def load_phoneme_converter(name: str, **kwargs):
        if name == 'gruut':
            return GruutPhonemizer()
        elif name == 'custom':
            return CustomPhonemizer()
        else:
            raise ValueError("Invalid phoneme converter.")