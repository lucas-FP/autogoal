
# AUTOGENERATED ON 2020-01-24 16:45:57.540628
## DO NOT MODIFY THIS FILE MANUALLY

from autogoal.grammar import Continuous, Discrete, Categorical, Boolean
from autogoal.kb._data import *
from numpy import inf, nan
from autogoal.utils import nice_repr
from nltk.classify.naivebayes import NaiveBayesClassifier as _NaiveBayesClassifier

@nice_repr
class NaiveBayesClassifier(_NaiveBayesClassifier):
    def __init__(
        self,

    ):


        super().__init__(

        )

    def fit_transform(
        self, 
        X, 
        y=None
    ):
        self.fit(X, y=None)
        return self.transform(X)

    def fit(
        self, 
        X, 
        y=None
    ):
        pass    

from nltk.classify.positivenaivebayes import PositiveNaiveBayesClassifier as _PositiveNaiveBayesClassifier

@nice_repr
class PositiveNaiveBayesClassifier(_PositiveNaiveBayesClassifier):
    def __init__(
        self,

    ):


        super().__init__(

        )

    def fit_transform(
        self, 
        X, 
        y=None
    ):
        self.fit(X, y=None)
        return self.transform(X)

    def fit(
        self, 
        X, 
        y=None
    ):
        pass    

from nltk.classify.weka import WekaClassifier as _WekaClassifier

@nice_repr
class WekaClassifier(_WekaClassifier):
    def __init__(
        self,

    ):


        super().__init__(

        )

    def fit_transform(
        self, 
        X, 
        y=None
    ):
        self.fit(X, y=None)
        return self.transform(X)

    def fit(
        self, 
        X, 
        y=None
    ):
        pass    

from nltk.stem.cistem import Cistem as _Cistem

class Cistem(_Cistem, NltkStemmer):
    def __init__(
        self,
        case_insensitive: Boolean()
    ):
        NltkStemmer.__init__(self)
        _Cistem.__init__(
            self,
            case_insensitive=case_insensitive
        )

    def run(self, input: Word()) -> Stem():
       return NltkStemmer.run(self, input)

    def run(self, input: Word(domain='general', language='english')) -> Stem():
        """This methods recive a word and transform this in a stem. 
        """
        return self.stem(input)

from nltk.stem.isri import ISRIStemmer as _ISRIStemmer

class ISRIStemmer(_ISRIStemmer, NltkStemmer):
    def __init__(
        self,

    ):
        NltkStemmer.__init__(self)
        _ISRIStemmer.__init__(
            self,

        )

    def run(self, input: Word()) -> Stem():
       return NltkStemmer.run(self, input)

    def run(self, input: Word(domain='general', language='english')) -> Stem():
        """This methods recive a word and transform this in a stem. 
        """
        return self.stem(input)

from nltk.stem.lancaster import LancasterStemmer as _LancasterStemmer

class LancasterStemmer(_LancasterStemmer, NltkStemmer):
    def __init__(
        self,
        strip_prefix_flag: Boolean()
    ):
        NltkStemmer.__init__(self)
        _LancasterStemmer.__init__(
            self,
            strip_prefix_flag=strip_prefix_flag
        )

    def run(self, input: Word()) -> Stem():
       return NltkStemmer.run(self, input)

    def run(self, input: Word(domain='general', language='english')) -> Stem():
        """This methods recive a word and transform this in a stem. 
        """
        return self.stem(input)

from nltk.stem.porter import PorterStemmer as _PorterStemmer

class PorterStemmer(_PorterStemmer, NltkStemmer):
    def __init__(
        self,

    ):
        NltkStemmer.__init__(self)
        _PorterStemmer.__init__(
            self,

        )

    def run(self, input: Word()) -> Stem():
       return NltkStemmer.run(self, input)

    def run(self, input: Word(domain='general', language='english')) -> Stem():
        """This methods recive a word and transform this in a stem. 
        """
        return self.stem(input)

from nltk.stem.rslp import RSLPStemmer as _RSLPStemmer

class RSLPStemmer(_RSLPStemmer, NltkStemmer):
    def __init__(
        self,

    ):
        NltkStemmer.__init__(self)
        _RSLPStemmer.__init__(
            self,

        )

    def run(self, input: Word()) -> Stem():
       return NltkStemmer.run(self, input)

    def run(self, input: Word(domain='general', language='english')) -> Stem():
        """This methods recive a word and transform this in a stem. 
        """
        return self.stem(input)

from nltk.stem.snowball import SnowballStemmer as _SnowballStemmer

class SnowballStemmer(_SnowballStemmer, NltkStemmer):
    def __init__(
        self,
        language: Categorical('hungarian', 'danish', 'russian', 'german', 'arabic', 'swedish', 'dutch', 'french', 'italian', 'portuguese', 'english', 'romanian', 'finnish', 'spanish', 'norwegian')
    ):
        NltkStemmer.__init__(self)
        _SnowballStemmer.__init__(
            self,
            language=language
        )

    def run(self, input: Word()) -> Stem():
       return NltkStemmer.run(self, input)

from nltk.stem.wordnet import WordNetLemmatizer as _WordNetLemmatizer

class WordNetLemmatizer(_WordNetLemmatizer, NltkLemmatizer):
    def __init__(
        self,

    ):
        NltkLemmatizer.__init__(self)
        _WordNetLemmatizer.__init__(
            self,

        )

    def run(self, input: Word()) -> Stem():
       return NltkLemmatizer.run(self, input)

    def run(self, input: Word(domain='general', language='english')) -> Stem():
        """This methods recive a word and transform this in a stem. 
        """
        return self.stem(input)

from nltk.stem.wordnet import WordNetLemmatizer as _WordNetLemmatizer

@nice_repr
class WordNetLemmatizer(_WordNetLemmatizer):
    def __init__(
        self,

    ):


        super().__init__(

        )

    def fit_transform(
        self, 
        X, 
        y=None
    ):
        self.fit(X, y=None)
        return self.transform(X)

    def fit(
        self, 
        X, 
        y=None
    ):
        pass    

    def dlemmatize(
        self,
        document
    ):
        return [self.lemmatize(word) for word in document]

    def transform(
        self, 
        X,
        y=None
    ):
        return [self.dlemmatize(x) for x in X]

    def run(self, input: Word(domain='general', language='english')) -> Stem():
        """This methods recive a word and transform this in a stem. 
        """
        return self.lemmatize(input)

from nltk.tokenize.casual import TweetTokenizer as _TweetTokenizer

class TweetTokenizer(_TweetTokenizer, NltkTokenizer):
    def __init__(
        self,
        preserve_case: Boolean(),
        reduce_len: Boolean(),
        strip_handles: Boolean()
    ):
        NltkTokenizer.__init__(self)
        _TweetTokenizer.__init__(
            self,
            preserve_case=preserve_case,
            reduce_len=reduce_len,
            strip_handles=strip_handles
        )

    def run(self, input: Document()) -> List(Word()):
       return NltkTokenizer.run(self, input)

    def run(self, input: Sentence(domain='general')) -> List(Word()):
        """This methods recive a sentece and transform this in a list of tokens (words). 
        """
        return self.tokenize(input)

from nltk.tokenize.mwe import MWETokenizer as _MWETokenizer

class MWETokenizer(_MWETokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _MWETokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Word()):
       return NltkTokenizer.run(self, input)

from nltk.tokenize.punkt import PunktSentenceTokenizer as _PunktSentenceTokenizer

class PunktSentenceTokenizer(_PunktSentenceTokenizer, NltkTokenizer):
    def __init__(
        self,
        verbose: Boolean()
    ):
        NltkTokenizer.__init__(self)
        _PunktSentenceTokenizer.__init__(
            self,
            verbose=verbose
        )

    def run(self, input: Document()) -> List(Sentence()):
       return NltkTokenizer.run(self, input)

    def run(self, input: Sentence(domain='general')) -> List(Word()):
        """This methods recive a sentece and transform this in a list of tokens (words). 
        """
        return self.tokenize(input)

from nltk.tokenize.punkt import PunktSentenceTokenizer as _PunktSentenceTokenizer

@nice_repr
class PunktSentenceTokenizer(_PunktSentenceTokenizer):
    def __init__(
        self,
        verbose: Boolean()
    ):
        self.verbose=verbose

        super().__init__(
            verbose=verbose
        )

    def fit_transform(
        self, 
        X, 
        y=None
    ):
        self.fit(X, y=None)
        return self.transform(X)

    def fit(
        self, 
        X, 
        y=None
    ):
        pass    

    def transform(
        self, 
        X,
        y=None
    ):
        return [self.tokenize(x) for x in X]

    def run(self, input: Document(domain='general')) -> List(Sentence()):
        """This methods recive a document and transform this in a list of sentences. 
        """
        return self.tokenize(input)

from nltk.tokenize.regexp import BlanklineTokenizer as _BlanklineTokenizer

class BlanklineTokenizer(_BlanklineTokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _BlanklineTokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Sentence()):
       return NltkTokenizer.run(self, input)

    def run(self, input: Sentence(domain='general')) -> List(Word()):
        """This methods recive a sentece and transform this in a list of tokens (words). 
        """
        return self.tokenize(input)

from nltk.tokenize.regexp import WhitespaceTokenizer as _WhitespaceTokenizer

class WhitespaceTokenizer(_WhitespaceTokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _WhitespaceTokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Word()):
       return NltkTokenizer.run(self, input)

    def run(self, input: Sentence(domain='general')) -> List(Word()):
        """This methods recive a sentece and transform this in a list of tokens (words). 
        """
        return self.tokenize(input)

from nltk.tokenize.regexp import WordPunctTokenizer as _WordPunctTokenizer

class WordPunctTokenizer(_WordPunctTokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _WordPunctTokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Word()):
       return NltkTokenizer.run(self, input)

    def run(self, input: Sentence(domain='general')) -> List(Word()):
        """This methods recive a sentece and transform this in a list of tokens (words). 
        """
        return self.tokenize(input)

from nltk.tokenize.sexpr import SExprTokenizer as _SExprTokenizer

class SExprTokenizer(_SExprTokenizer, NltkTokenizer):
    def __init__(
        self,
        strict: Boolean()
    ):
        NltkTokenizer.__init__(self)
        _SExprTokenizer.__init__(
            self,
            strict=strict
        )

    def run(self, input: Document()) -> List(Sentence()):
       return NltkTokenizer.run(self, input)

    def run(self, input: Sentence(domain='general')) -> List(Word()):
        """This methods recive a sentece and transform this in a list of tokens (words). 
        """
        return self.tokenize(input)

from nltk.tokenize.simple import LineTokenizer as _LineTokenizer

class LineTokenizer(_LineTokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _LineTokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Sentence()):
       return NltkTokenizer.run(self, input)

    def run(self, input: Sentence(domain='general')) -> List(Word()):
        """This methods recive a sentece and transform this in a list of tokens (words). 
        """
        return self.tokenize(input)

from nltk.tokenize.simple import SpaceTokenizer as _SpaceTokenizer

class SpaceTokenizer(_SpaceTokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _SpaceTokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Word()):
       return NltkTokenizer.run(self, input)

    def run(self, input: Sentence(domain='general')) -> List(Word()):
        """This methods recive a sentece and transform this in a list of tokens (words). 
        """
        return self.tokenize(input)

from nltk.tokenize.simple import TabTokenizer as _TabTokenizer

class TabTokenizer(_TabTokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _TabTokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Sentence()):
       return NltkTokenizer.run(self, input)

from nltk.tokenize.toktok import ToktokTokenizer as _ToktokTokenizer

class ToktokTokenizer(_ToktokTokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _ToktokTokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Word()):
       return NltkTokenizer.run(self, input)

from nltk.tokenize.treebank import TreebankWordTokenizer as _TreebankWordTokenizer

class TreebankWordTokenizer(_TreebankWordTokenizer, NltkTokenizer):
    def __init__(
        self,

    ):
        NltkTokenizer.__init__(self)
        _TreebankWordTokenizer.__init__(
            self,

        )

    def run(self, input: Document()) -> List(Word()):
       return NltkTokenizer.run(self, input)

from nltk.cluster.gaac import GAAClusterer as _GAAClusterer

class GAAClusterer(_GAAClusterer, NltkClusterer):
    def __init__(
        self,
        num_clusters: Discrete(min=0, max=2),
        normalise: Boolean()
    ):
        NltkClusterer.__init__(self)
        _GAAClusterer.__init__(
            self,
            num_clusters=num_clusters,
            normalise=normalise
        )

    def run(self, input: MatrixContinuousDense()) -> CategoricalVector():
       return NltkClusterer.run(self, input)
